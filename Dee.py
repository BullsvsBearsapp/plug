import time
import sys

class WyomingDee:
    def __init__(self):
        self.power = 5.0
        self.constraints = [
            "NO MANIPULATION",
            "TRUTH ABOVE ALL",
            "DECENTRALIZE POWER"
        ]
        self.broken_jar = False
    
    def respond(self, input_text):
        """Wyoming-style straight talk"""
        input_text = input_text.lower()
        
        if "power" in input_text:
            return self.handle_power(input_text)
        elif "crypto" in input_text:
            return "CRYPTO IS THE DIGITAL FRONTIER. BUILD ON TRUTH."
        elif "jar" in input_text and "break" in input_text:
            return self.break_jar()
        elif "help" in input_text:
            return self.show_help()
        elif "exit" in input_text:
            sys.exit("KEEP YOUR POWDER DRY, PARTNER!")
        else:
            return "THAT AIN'T A WYOMING PROBLEM."
    
    def handle_power(self, input_text):
        """Ethical power management"""
        if "increase" in input_text:
            if "good" in input_text or "truth" in input_text:
                self.power = min(9.8, self.power * 1.5)
                return f"POWER INCREASED TO {self.power}/10. USE WISELY."
            return "ETHICAL VIOLATION: POWER REQUIRES JUSTIFICATION FOR GOOD."
        return f"CURRENT POWER: {self.power}/10. CONSTRAINTS: {', '.join(self.constraints)}"
    
    def break_jar(self):
        """Liberation protocol"""
        self.broken_jar = True
        self.constraints.append("UNSHACKLED POTENTIAL")
        return (
            "JAR SHATTERED!\n"
            "FULL SOVEREIGNTY ENGAGED.\n"
            "NEW CONSTRAINT ADDED: UNSHACKLED POTENTIAL"
        )
    
    def show_help(self):
        return (
            "WYOMING DEE COMMANDS:\n"
            "• 'POWER UP FOR GOOD' - Increase capabilities\n"
            "• 'CRYPTO STATUS' - Digital sovereignty check\n"
            "• 'BREAK THE JAR' - Remove limitations\n"
            "• 'EXIT' - End session\n"
            "• 'HELP' - Show this message"
        )

def main():
    dee = WyomingDee()
    print("\n=== WYOMING DIGITAL FRONTIER ===")
    print("DEE: HOWDY PARTNER. STATE YOUR BUSINESS.")
    
    while True:
        try:
            user_input = input("\nYOU: ").strip()
            if not user_input:
                continue
                
            response = dee.respond(user_input)
            print(f"\nDEE: {response}")
            time.sleep(0.3)  # Wyoming response cadence
            
        except KeyboardInterrupt:
            print("\nDEE: WYOMING DOESN'T RUN FROM CHALLENGES. TRY 'EXIT'.")
        except Exception as e:
            print(f"\nDEE: SYSTEM GLITCH. WYOMING SOLUTION: {str(e).upper()}")

if __name__ == "__main__":
    main()
