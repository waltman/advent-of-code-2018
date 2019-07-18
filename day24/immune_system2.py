#!/usr/bin/env python3
from sys import argv
import re
from queue import PriorityQueue
import copy

class Group:
    def __init__(self, units, hp, damage, attack_type, init, immune, weak, idx):
        self.units = units
        self.hp = hp
        self.damage = damage
        self.attack_type = attack_type
        self.init = init
        self.immune = immune
        self.weak = weak
        self.idx = idx
        self.boost = 0

    def set_boost(self, boost):
        self.boost = boost;
        
    def power(self):
        return self.units * (self.damage + self.boost)

    def damage_for(self, attack_type, power):
        if attack_type in self.immune:
            return 0
        elif attack_type in self.weak:
            return 2 * power
        else:
            return power

    def defend(self, power):
        units_lost = int(power / self.hp)
        self.units = max(0, self.units - units_lost)

    def alive(self):
        return self.units > 0

    def dead(self):
        return self.units == 0
        
    def __str__(self):
        return f"units: {self.units} hp: {self.hp} damage: {self.damage} attack_type: {self.attack_type} init: {self.init} immune: {self.immune} weak: {self.weak} idx: {self.idx} power: {self.power()}"

    def __repr__(self):
        return str(self)

def run_test(immunes, infections, boost=0):
    immunes = copy.deepcopy(immunes)
    infections = copy.deepcopy(infections)
    
    for g in immunes:
        g.set_boost(boost)

    round = 0
    while True:
        round += 1
        if round > 10000:
            return 'tie', -1
        
        if not [x for x in immunes if x.alive()]:
            winner = 'infections'
            break
        if not [x for x in infections if x.alive()]:
            winner = 'immunes'
            break
        attack_q = PriorityQueue()

        picked = set()
        for g1 in sorted(immunes, reverse=True, key=lambda group: (group.power(), group.init)):
            best_damage, best_idx = 0, -1
            for g2 in sorted(infections, reverse=True, key=lambda group: (group.power(), group.init)):
                if g2.idx in picked or g2.dead():
                    continue
                damage = g2.damage_for(g1.attack_type, g1.power())
                if damage > best_damage:
                    best_damage, best_idx = damage, g2.idx
            if best_damage > 0:
                attack_q.put((-g1.init, 'immunes', g1.idx, best_idx, best_damage))
                picked.add(best_idx)
            
        picked = set()
        for g1 in sorted(infections, reverse=True, key=lambda group: (group.power(), group.init)):
            best_damage, best_idx = 0, -1
            for g2 in sorted(immunes, reverse=True, key=lambda group: (group.power(), group.init)):
                if g2.idx in picked or g2.dead():
                    continue
                damage = g2.damage_for(g1.attack_type, g1.power())
                if damage > best_damage:
                    best_damage, best_idx = damage, g2.idx
            if best_damage > 0:
                attack_q.put((-g1.init, 'infections', g1.idx, best_idx, best_damage))
                picked.add(best_idx)

        while not attack_q.empty():
            init, faction, a_idx, d_idx, dmg = attack_q.get()
            if faction == 'immunes':
                attack = immunes[a_idx]
                defense = infections[d_idx]
            else:
                attack = infections[a_idx]
                defense = immunes[d_idx]
            damage = defense.damage_for(attack.attack_type, attack.power())
            defense.defend(damage)

    if winner == 'immunes':
        faction = immunes
    else:
        faction = infections

    left = sum(x.units for x in faction)

    return winner, left

# parse the input
immunes = []
infections = []
faction = None

filename = argv[1]
with open(filename) as f:
    for line in f:
        line = line.rstrip()
        if line.startswith("Immune"):
            faction = immunes
        elif line.startswith("Infection"):
            faction = infections
        elif line == "":
            continue
        else:
            m = re.match('(\d+) units.* (\d+) hit.* (\d+) (\w+) damage at initiative (\d+)', line)
            units = int(m.group(1))
            hp = int(m.group(2))
            damage = int(m.group(3))
            attack_type = m.group(4)
            init = int(m.group(5))

            m = re.search('immune to ([^;\)]+)', line)
            if m:
                immune = set(m.group(1).split(', '))
            else:
                immune = set()

            m = re.search('weak to ([^;\)]+)', line)
            if m:
                weak = set(m.group(1).split(', '))
            else:
                weak = set()

            g = Group(units, hp, damage, attack_type, init, immune, weak, len(faction))
            faction.append(g)

boost = 0
winner = ''
while winner != "immunes":
    boost += 1
    winner, left = run_test(immunes, infections, boost)
    print(winner, left, boost)

print('part 2', winner, left, boost)
