import random
import string

class ConsolePasswordGenerator:
    def generate_password(self, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def run(self):
        length = int(input("Enter the desired length of the password: "))
        password = self.generate_password(length)
        print("Generated Password:", password)


if __name__ == "__main__":
    password_generator = ConsolePasswordGenerator()
    password_generator.run()
