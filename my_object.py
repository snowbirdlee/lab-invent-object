from dataclasses import dataclass, field
import time

@dataclass
class Squishmallow():
    name: str
    size: int = 1
    price: float = 0.00
    color: str = "white"
    eyes_open: bool = field(default = False, init = False)
    size_string: str = "small"

    def set_size(self, size: int):
        self.size = size
        if self.size == 1:
            self.size_string = "small"
        elif self.size == 2:
            self.size_string = "medium"
        elif self.size == 3:
            self.size_string = "large"
        elif self.size == 4:
            self.size_string = "extra large"
    def set_price(self, price: float):
        self.price = price
    def set_color(self, color: str):
        self.color = color
    def eyes_opened(self):
        self.eyes_open = True
    def eyes_closed(self):
        self.eyes_open = False
    def status(self):
        if self.eyes_open:
            if self.size_string == "extra large":
                print(f"{self.name.title()} is now an ${self.price:.2f} {self.size_string}, {self.color} Squishmallow whose eyes are open.")
            else:
                print(f"{self.name.title()} is now a ${self.price:.2f} {self.size_string}, {self.color} Squishmallow whose eyes are open.")
        else:
            if self.size_string == "extra large":
                print(f"{self.name.title()} is now an ${self.price:.2f} {self.size_string}, {self.color} Squishmallow whose eyes are open.")
            else:
                print(f"{self.name.title()} is now a ${self.price:.2f} {self.size_string}, {self.color} Squishmallow whose eyes are closed.")
    def inflation(self):
        self.price = self.price + 1
    def time_to_sleep(self):
        self.eyes_open = False
    def wake_up(self):
        self.eyes_open = True
    def eat(self):
        self.size = self.size + 1
        if self.size == 1:
            self.size_string = "small"
        elif self.size == 2:
            self.size_string = "medium"
        elif self.size == 3:
            self.size_string = "large"
        elif self.size == 4:
            self.size_string = "extra large"

def main():
    
    buttons = Squishmallow("buttons")
    buttons.set_size(2)
    buttons.set_price(8.99)
    buttons.set_color("blue")
    buttons.eyes_closed()
    buttons.status()
    time.sleep(2)

    buttons.inflation()
    print("\nThere's inflation in the market! Buttons went up $1...")
    time.sleep(1)
    print(f"Current price of Buttons: ${buttons.price:.2f}")
    time.sleep(1)

    buttons.wake_up()
    print("\nButtons is waking up...")
    time.sleep(3)
    print("Buttons is up! His eyes are open!")
    time.sleep(1)
    
    buttons.eat()
    print("\nButtons is eating...")
    time.sleep(3)
    print(f"Buttons is full! He is now {buttons.size_string}.\n")
    time.sleep(1)
    
    buttons.status()

if __name__ == "__main__":
    main()
