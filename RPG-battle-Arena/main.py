import random

class Player:
    def __init__(self, name):
        self.name = name
        self.hp = 100
        self.max_hp = 100
        self.attack = 15
        self.level = 1
        self.xp = 0
        self.gold = 0

    def heal(self):
        amount = random.randint(15, 30)
        self.hp = min(self.max_hp, self.hp + amount)
        print(f"\n❤️ You healed {amount} HP!")

    def gain_rewards(self):
        xp = random.randint(20, 40)
        gold = random.randint(10, 30)

        self.xp += xp
        self.gold += gold

        print(f"\n🎉 +{xp} XP")
        print(f"💰 +{gold} Gold")

        if self.xp >= self.level * 100:
            self.level += 1
            self.max_hp += 20
            self.hp = self.max_hp
            self.attack += 5

            print("\n⬆️ LEVEL UP!")
            print(f"You reached Level {self.level}!")

class Enemy:
    def __init__(self):
        names = ["Goblin", "Orc", "Skeleton", "Bandit", "Dark Mage"]

        self.name = random.choice(names)
        self.hp = random.randint(40, 80)
        self.attack = random.randint(8, 15)

def battle(player):
    enemy = Enemy()

    print(f"\n👹 A {enemy.name} appeared!")
    print(f"❤️ Enemy HP: {enemy.hp}")

    while enemy.hp > 0 and player.hp > 0:

        print("\n" + "=" * 30)
        print(f"{player.name} HP: {player.hp}/{player.max_hp}")
        print(f"{enemy.name} HP: {enemy.hp}")
        print("=" * 30)

        print("1. Attack")
        print("2. Heal")

        choice = input("\nChoose: ")

        if choice == "1":

            damage = random.randint(
                player.attack - 5,
                player.attack + 5
            )

            if random.randint(1, 100) <= 20:
                damage *= 2
                print("\n💥 CRITICAL HIT!")

            enemy.hp -= damage

            print(f"⚔️ You dealt {damage} damage!")

        elif choice == "2":
            player.heal()

        else:
            print("Invalid choice!")
            continue

        if enemy.hp <= 0:
            print(f"\n🏆 {enemy.name} defeated!")
            player.gain_rewards()
            return

        enemy_damage = random.randint(
            enemy.attack - 3,
            enemy.attack + 3
        )

        player.hp -= enemy_damage

        print(
            f"👹 {enemy.name} dealt "
            f"{enemy_damage} damage!"
        )

    if player.hp <= 0:
        print("\n💀 GAME OVER")
        exit()

def main():
    print("=" * 35)
    print("⚔️ RPG BATTLE ARENA ⚔️")
    print("=" * 35)

    name = input("Enter your name: ")

    player = Player(name)

    while True:

        print("\n")
        print("1. Fight Enemy")
        print("2. View Stats")
        print("3. Exit")

        choice = input("\nChoose: ")

        if choice == "1":
            battle(player)

        elif choice == "2":

            print("\n📊 PLAYER STATS")
            print(f"Name : {player.name}")
            print(f"Level: {player.level}")
            print(f"HP   : {player.hp}/{player.max_hp}")
            print(f"ATK  : {player.attack}")
            print(f"XP   : {player.xp}")
            print(f"Gold : {player.gold}")

        elif choice == "3":
            print("\n👋 Thanks for playing!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()