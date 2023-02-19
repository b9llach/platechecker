import requests
import threading
                    
def main(starting_letter: str, ending_plate: str):
    print(starting_letter, ending_plate)
    starting = False
    state_acronyms = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 
                            'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 
                            'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 
                            'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 
                            'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 
                            'VA', 'WA', 'WV', 'WI', 'WY']
    alphabet = [ 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]
    with open("available.txt","a") as f:
        for i in state_acronyms:
            for a in alphabet:
                if a == starting_letter or starting == True:
                    starting = True
                    for b in alphabet:
                        for c in alphabet:
                            url = f"https://www.dmv.ca.gov/wasapp/ipp2/initPers.do?plate={a}{b}{c}&state={i}"
                            response = requests.get(url)
                            if "Results Found" in response.text:
                                print(f"{a}{b}{c} available in {i}\n")
                                f.write(f"{a}{b}{c} available in {i}")
                                    
                            else:
                                print(f"{a}{b}{c} not available in {i}")
                            if f"{a}{b}{c}" == ending_plate.upper():
                                return
                        
if __name__ == "__main__":
    f = open("available.txt","w")
    f.close()
    t1 = threading.Thread(target=main, args=("A","IZZ",))
    t2 = threading.Thread(target=main, args=("J","RZZ"))
    t3 = threading.Thread(target=main, args=("S","ZZZ"))
    t1.start()
    t2.start()
    t3.start()
        