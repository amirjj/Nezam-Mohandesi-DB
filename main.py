from attacker import Attacker
from parser_app import parser

if __name__ == "__main__":
    atck = Attacker(1)
    atck.run()
    all_data = parser.crawl()
    parser.dump_to_csv(all_data)

