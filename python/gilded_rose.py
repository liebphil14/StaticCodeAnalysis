# -*- coding: utf-8 -*-
"""Gilded Rose inventory system."""

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
CONJURED = "Conjured Mana Cake"


class GildedRose:
    """Handles item updates."""

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        """Update quality and sell_in values."""
        for item in self.items:

            if item.name not in (AGED_BRIE, BACKSTAGE):
                if item.quality > 0 and item.name != SULFURAS:
                    if item.name == CONJURED:
                        item.quality -= 2
                    else:
                        item.quality -= 1

            else:
                if item.quality < 50:
                    item.quality += 1

                    if item.name == BACKSTAGE:
                        if item.sell_in < 11 and item.quality < 50:
                            item.quality += 1

                        if item.sell_in < 6 and item.quality < 50:
                            item.quality += 1

            if item.name != SULFURAS:
                item.sell_in -= 1

            if item.sell_in < 0:
                if item.name == BACKSTAGE:
                    item.quality = 0
                elif item.name == AGED_BRIE:
                    if item.quality < 50:
                        item.quality += 1
                elif item.quality > 0 and item.name != SULFURAS:
                    if item.name == CONJURED:
                        item.quality -= 2
                    else:
                        item.quality -= 1


class Item:
    """Represents an inventory item."""

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"