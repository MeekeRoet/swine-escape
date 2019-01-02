import numpy as np
import pandas as pd
import itertools
import sys


class SwineEscape:

    def __init__(self, board_size=12, swine_start=7, butcher_start=1):
        if butcher_start >= swine_start:
            raise ValueError('Error in starting positions: The swine has to start ahead of the butcher.')
        elif swine_start >= board_size:
            raise ValueError('Error in starting positions: The river has to lie ahead of the swine.')
        else:
            self.board_size = board_size
            self.swine_start = swine_start
            self.butcher_start = butcher_start

    def _create_probs_df(self):
        swine_positions = np.arange(self.swine_start, self.board_size+1)
        butcher_positions = np.arange(self.butcher_start, self.board_size+1)
        self.probs = pd.DataFrame(np.nan * np.ones(shape=(len(swine_positions), len(butcher_positions))),
                                  index=swine_positions, columns=butcher_positions)

    def _fill_known_probs(self):
        # Swine has won with 100% probability if end of board is reached.
        self.probs.loc[self.board_size, :] = 1.0

        # Swine wins with 0% probability if the butcher is ahead or at the same square.
        # I.e. upper right triangle should be zeros.
        mask = np.ones(self.probs.shape, dtype='bool')
        triu = np.triu_indices(n=self.probs.shape[0], m=self.probs.shape[0])
        mask[tuple([triu[0], triu[1] + self.probs.shape[1] - self.probs.shape[0]])] = False
        self.probs.where(mask, other=0.0, inplace=True)

    def _F(self, sp, bp):
        """Calculate the swine's probability of winning based on the current swine and butcher position.

        Arguments
            - sp:    swine's current position
            - bp:    butcher's current position
        """

        # Check that the current positions are not lower than the starting positions.
        if sp < self.probs.index.min():
            sp = self.probs.index.min()
            print('Swine position lower than starting position: using swine starting position ({}) instead.'.format(self.swine_start))
        if bp < self.probs.columns.min():
            bp = self.probs.columns.min()
            print('Butcher position lower than starting position: using butcher starting position ({}) instead.'.format(self.butcher_start))

        # Check that neither the swine nor the butcher has already reached the end of the board.
        # If so, reset position to the last space on the board.
        if sp > self.probs.index.max():
            sp = self.probs.index.max()
        if bp > self.probs.columns.max():
            bp = self.probs.columns.max()

        # If the requested probability is already known: return from storage.
        if not np.isnan(self.probs.loc[sp, bp]):
            return self.probs.loc[sp, bp]

        # Else: calculate the requested probability according to the DP recurrence, store and return.
        else:
            prob = 1/6 * self._F(sp+1, bp) \
                   + 1/6 * self._F(sp+2, bp) \
                   + 1/6 * self._F(sp+3, bp) \
                   + 1/6 * self._F(sp+1, bp+1) \
                   + 1/6 * self._F(sp, bp+5) \
                   + 1/6 * self._F(sp, bp+6)

            self.probs.loc[sp, bp] = prob

            return prob

    def _create_transition_matrix(self):
        # Get state space.
        self.states = list(
            itertools.product(range(self.butcher_start, self.board_size+1),
                              range(self.swine_start, self.board_size+1)))

        # Filter out invalid states (butcher ahead of swine).
        self.states = list(itertools.compress(self.states, [i[0] <= i[1] for i in self.states]))

        # Initiate transition matrix.
        self.tm = pd.DataFrame(np.zeros(shape=(len(self.states), len(self.states))),
                               index=self.states,
                               columns=self.states)

        # Loop over states to fill in transition probabilities.
        for b, s in self.states:

            # If someone already won, set as absorbing state.
            if s == self.board_size or b == s:
                self.tm.loc[[(b, s)], [(b, s)]] += 1
                continue

            # Die outcome 1.
            self.tm.loc[[(b, s)], [(b, s+1)]] += 1/6

            # Die outcome 2.
            if s+2 > self.board_size:
                self.tm.loc[[(b, s)], [(b, self.board_size)]] += 1/6
            else:
                self.tm.loc[[(b, s)], [(b, s+2)]] += 1/6

            # Die outcome 3.
            if s+3 > self.board_size:
                self.tm.loc[[(b, s)], [(b, self.board_size)]] += 1/6
            else:
                self.tm.loc[[(b, s)], [(b, s+3)]] += 1/6

            # Die outcome 4.
            self.tm.loc[[(b, s)], [(b+1, s+1)]] += 1/6

            # Die outcome 5.
            if b+5 > s:
                self.tm.loc[[(b, s)], [(s, s)]] += 1/6
            else:
                self.tm.loc[[(b, s)], [(b+5, s)]] += 1/6

            # Die outcome 6.
            if b+6 > s:
                self.tm.loc[[(b, s)], [(s, s)]] += 1/6
            else:
                self.tm.loc[[(b, s)], [(b+6, s)]] += 1/6

    def _solve_markov_chain(self):
        max_turns = (self.board_size - self.swine_start) + int(
            (self.board_size - 2 - self.butcher_start) / 5)  # Calculate the maximum number of turns.
        tm_final = pd.DataFrame(np.matrix(self.tm) ** (max_turns),
                                index=self.states,
                                columns=self.states)  # Get final transition matrix.
        swine_win_prob = 0
        butcher_win_prob = 0

        for b, s in self.states:
            if b == s:
                butcher_win_prob += tm_final.at[(self.butcher_start, self.swine_start), (b, s)]
            else:
                swine_win_prob += tm_final.at[(self.butcher_start, self.swine_start), (b, s)]

        return swine_win_prob

    def solve_game(self, method):
        if method == 'dp':
            self._create_probs_df()
            self._fill_known_probs()
            self.winning_prob = self._F(self.swine_start, self.butcher_start)
            return self.winning_prob

        elif method == 'markov':
            self._create_transition_matrix()
            self.winning_prob = self._solve_markov_chain()
            return self.winning_prob

        else:
            raise ValueError('{} is not implemented as a method, please choose from dp or markov.'.format(method))