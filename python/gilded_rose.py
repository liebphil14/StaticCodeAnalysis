# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE = "Backstage passes to a TAFKAL80ETC concert"
CONJURED = "Conjured Mana Cake"

class GildedRose:

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name not in (AGED_BRIE, BACKSTAGE):
                if item.quality > 0:
                    if item.name not in (SULFURAS):
                        if item.name == CONJURED:
                            item.quality -= 2
                        else:
                            item.quality -= 1
            else:
                if item.quality < 50:
                    item.quality += 1
                    if item.name == BACKSTAGE:
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality += 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality += 1
            if item.name not in (SULFURAS):
                item.sell_in -= 1
            if item.sell_in < 0:
                if item.name not in (AGED_BRIE):
                    if item.name not in (BACKSTAGE):
                        if item.quality > 0:
                            if item.name not in (SULFURAS):
                                if item.name == CONJURED:
                                    item.quality -= 2
                                else:
                                    item.quality -= 1
                    else:
                        item.quality = 0
                else:
                    if item.quality < 50:
                        item.quality += 1

    
class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return f"{self.name}, {self.sell_in}, {self.quality}"
