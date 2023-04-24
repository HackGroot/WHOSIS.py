import whois

def main():
    # Get the domain name
    domain_name = input("Enter the domain name: ")

    # Get the WHOIS information for the domain name
    whois_info = whois.whois(domain_name)

    # Print the WHOIS information
    print("WHOIS information for {}:".format(domain_name))
    for key, value in whois_info.items():
        print("  {}: {}".format(key, value))

if __name__ == "__main__":
    main()

