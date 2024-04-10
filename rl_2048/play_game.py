"""Script to play a single game from a checkpoint."""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from game.play import Play
from learning import learning
from learning.model import FeedModel
from learning.Strategies import Strategies

import tensorflow as tf
import numpy as np


def average_score(strategy, window=None):
    """Plays a number of games, returns average score."""

    scores = []
    for _ in range(window.config.get_num_games()):
        score, _ = Play.play_game(strategy, window=window)
        scores.append(score)
    return np.mean(scores)


def make_greedy_strategy(train_dir):
    """Load the latest checkpoint from train_dir, make a greedy strategy."""

    session = tf.Session()
    model = FeedModel()
    saver = tf.train.Saver()
    print(train_dir)
    saver.restore(session, tf.train.latest_checkpoint(train_dir))

    get_q_values = learning.make_get_q_values(session, model)
    greedy_strategy = Strategies.make_greedy_strategy(get_q_values)

    return greedy_strategy
