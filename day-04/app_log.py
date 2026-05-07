# Function banaya gaya hai log file read karne ke liye
def read_logs(file_name):

    # try block use karte hain kyuki file operations fail ho sakte hain
    # Example:
    # - file exist nahi karti
    # - permission issue
    # - corrupted file
    try:

        # with open() safest way hai file handle karne ka
        #
        # file_name -> kaunsi file open karni hai
        # "r" -> read mode
        # as file -> opened file ko "file" variable me store karna
        #
        # with ka benefit:
        # file automatically close ho jaati hai
        with open(file_name, "r") as file:

            # readlines() file ki saari lines ko read karta hai
            # aur ek list me convert kar deta hai
            #
            # Example:
            # [
            #   "INFO Server started\n",
            #   "ERROR Database failed\n"
            # ]
            logs = file.readlines()

            # Check kar rahe hain file empty toh nahi
            #
            # if not logs ka matlab:
            # logs list empty hai
            if not logs:

                # User ko message show karo
                print("Log file is empty.")

                # None return karke function stop kar do
                return None

            # Agar logs successfully mil gaye
            # toh logs return karo
            return logs

    # Agar file exist nahi karti toh ye block chalega
    except FileNotFoundError:

        # Friendly error message print karo
        print("Log file not found.")

        # None return karo kyuki logs read nahi hue
        return None

    # Generic exception handling
    # unexpected errors catch karne ke liye
    except Exception as error:

        # Actual error dynamically print hoga
        print(f"An error occurred while reading the file: {error}")

        # Function fail hua toh None return karo
        return None


# Ye function logs analyze karega
# aur INFO/WARNING/ERROR count karega
def analyze_logs(logs):

    # Dictionary use kar rahe hain counts store karne ke liye
    #
    # Key -> log type
    # Value -> count
    #
    # Initial count sabka 0 hai
    log_counts = {
        "INFO": 0,
        "WARNING": 0,
        "ERROR": 0
    }

    # for loop har line pe chalega
    for line in logs:

        # Check karo current line me INFO present hai ya nahi
        if "INFO" in line:

            # INFO count increase karo
            #
            # += 1 matlab:
            # existing value me 1 add karo
            log_counts["INFO"] += 1

        # Check karo WARNING present hai ya nahi
        elif "WARNING" in line:

            # WARNING count increase karo
            log_counts["WARNING"] += 1

        # Check karo ERROR present hai ya nahi
        elif "ERROR" in line:

            # ERROR count increase karo
            log_counts["ERROR"] += 1

    # Final counts return karo
    return log_counts


# Ye function terminal me summary print karega
def display_summary(log_counts):

    # \n new line create karta hai
    print("\nLog Summary")

    # Decorative line print karne ke liye
    # "-" * 20 matlab dash 20 times print karo
    print("-" * 20)

    # f-string use karke dynamic values print kar rahe hain
    #
    # Example:
    # INFO: 10
    print(f"INFO: {log_counts['INFO']}")
    print(f"WARNING: {log_counts['WARNING']}")
    print(f"ERROR: {log_counts['ERROR']}")


# Ye function summary ko output file me write karega
def write_summary(log_counts, output_file):

    # try block use kar rahe hain
    # kyuki file writing fail ho sakti hai
    try:

        # Output file open karo write mode me
        #
        # "w" mode:
        # - file create karega agar exist nahi karti
        # - overwrite karega agar already exist karti hai
        with open(output_file, "w") as file:

            # Heading write karo
            file.write("Log Summary\n")

            # Decorative line write karo
            file.write("-" * 20 + "\n")

            # INFO count file me write karo
            file.write(f"INFO: {log_counts['INFO']}\n")

            # WARNING count write karo
            file.write(f"WARNING: {log_counts['WARNING']}\n")

            # ERROR count write karo
            file.write(f"ERROR: {log_counts['ERROR']}\n")

        # Success message print karo
        print(f"\nSummary written to {output_file}")

    # Agar koi error aaye toh handle karo
    except Exception as error:

        # Actual error show karo
        print(f"An error occurred while writing the file: {error}")


# main() pure program ka controller hai
def main():

    # Input log file ka naam
    input_file = "app.log"

    # Output summary file ka naam
    output_file = "log_summary.txt"

    # read_logs() function call karo
    # aur returned logs ko logs variable me store karo
    logs = read_logs(input_file)

    # Agar logs None hain matlab:
    # - file missing hai
    # - ya file empty hai
    #
    # Toh program yahi stop kar do
    if logs is None:
        return

    # Logs analyze karo
    # aur counts store karo
    log_counts = analyze_logs(logs)

    # Terminal me summary print karo
    display_summary(log_counts)

    # Summary output file me save karo
    write_summary(log_counts, output_file)


# Ye professional Python structure hai
# Ye check karta hai:
# "Kya ye file directly run hui hai?"
#
# Agar YES:
# toh main() execute hoga
if __name__ == "__main__":

    # Program start karo
    main()