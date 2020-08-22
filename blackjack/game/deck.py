# -*- coding: utf-8 -*-

from random import shuffle

from .card import Card
from lang.language import translate

__author__ = 'Rico'


class Deck(object):

    def __init__(self, lang_id="en"):
        self.lang_id = lang_id
        self.value_str = [translate("ace", lang_id), "2", "3", "4", "5", "6", "7", "8", "9", "10",
                          translate("jack", lang_id), translate("queen", lang_id), translate("king", lang_id)]
        self._cards = []
        self._set_up_deck()
        self._shuffle()

    def _set_up_deck(self):
        self._cards = []

        for card_id in range(52):
            card = Card(card_id, self.value_str)
            self._cards.append(card)

    def _shuffle(self):
        shuffle(self._cards)

    @property
    def cards(self):
        return self._cards

    def pick_one_card(self):
        # TODO if len(self._cards) <= 0, then raise error
        return self._cards.pop(0)
