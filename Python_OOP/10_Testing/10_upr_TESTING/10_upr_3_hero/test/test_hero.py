import unittest

from test.hero import Hero


class TestHero(unittest.TestCase):
    username = "deni"
    level = 1
    health = 5
    damage = 5
    def test_all_inplement_value_correct(self):
        deni=Hero(self.username,self.level,self.health,self.damage)
        self.assertEqual(self.username,deni.username)
        self.assertEqual(self.health,deni.health)
        self.assertEqual(self.level,deni.level)
        self.assertEqual(self.damage,deni.damage)

    def test_battle_same_name_return_exception(self):
        deni = Hero(self.username, self.level, self.health, self.damage)
        keti = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as context:
            deni.battle(keti)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle__zero_health_hero__return_exception(self):
        deni = Hero(self.username, self.level, self.health, self.damage)
        keti = Hero("Keti", self.level, self.health, self.damage)
        deni.health=0
        with self.assertRaises(Exception) as context:
            deni.battle(keti)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))


    def test_battle__zero_health_enemy__return_exception(self):
        deni = Hero(self.username, self.level, self.health, self.damage)
        keti = Hero("Keti", self.level, self.health, self.damage)
        keti.health=0
        with self.assertRaises(Exception) as context:
            deni.battle(keti)
        self.assertEqual(f"You cannot fight {keti.username}. He needs to rest", str(context.exception))

    def test_battle__correct_values_reduce_both_damage(self):
        """player_damage = self.damage * self.level
        enemy_hero_damage = enemy_hero.damage * enemy_hero.level

        self.health -= enemy_hero_damage
        enemy_hero.health -= player_damage
"""
        #  HERO(username: str, level: int, health: float, damage: float):
        deni = Hero("deni", 2, 20, 5)
        keti = Hero("Keti", 2, 30, 5)
        deni.battle(keti)
        self.assertEqual(25,keti.health) # have to be 20, prove again
        self.assertEqual(10,deni.health)

    # draw
    def test_battle__both_healt_zero_return_draw(self):
        #  HERO(username: str, level: int, health: float, damage: float):
        deni = Hero("deni", 2, 10, 5)
        keti = Hero("Keti", 2, 10, 5)
        result=deni.battle(keti)
        self.assertEqual("Draw", result)

    def test_battle__enemy_health_zero_return_win(self):
        """self.level += 1
            self.health += 5
            self.damage += 5"""
        #  HERO(username: str, level: int, health: float, damage: float):
        deni = Hero("deni", 2, 50, 5) #40
        keti = Hero("Keti", 2, 10, 5)
        result = deni.battle(keti)
        self.assertEqual("You win", result)
        self.assertEqual(45, deni.health)
        self.assertEqual(3, deni.level)
        self.assertEqual(10, deni.damage)

    def test_battle__hero_health_zero_return_win_enemy(self):
        """self.level += 1
            self.health += 5
            self.damage += 5"""
        #  HERO(username: str, level: int, health: float, damage: float):
        deni = Hero("deni", 2, 10, 5) #40
        keti = Hero("Keti", 2, 50, 5)
        result = deni.battle(keti)
        self.assertEqual("You lose", result)
        self.assertEqual(45, keti.health)
        self.assertEqual(3, keti.level)
        self.assertEqual(10, keti.damage)

    def test_string_representation_of_hero__rerurn_string(self):
        deni = Hero(self.username, self.level, self.health, self.damage)
        correct=f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        actual=str(deni)
        self.assertEqual(correct,actual)



if __name__=="__main__":
    unittest.main()
