
import sys
import csv

learningReate: int = 5

def main() -> int:
    
    with open(sys.argv[1], newline='') as csvfile:
        fieldnames = ['km', 'price']
        data = csv.DictReader(csvfile, fieldnames=fieldnames)
        for field in data:
            print(field['km'], field['price'])
        
    return 0


if __name__ == "__main__":
    sys.exit(main())