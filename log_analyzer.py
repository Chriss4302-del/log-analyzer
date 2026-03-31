def analyze_log(file_path):
    failed_logins = 0
    successful_logins = 0

    with open(file_path, "r") as file:
        for line in file:
            if "Failed password" in line:
                failed_logins += 1
            elif "Accepted" in line:
                successful_logins += 1

    print("Log Analysis Summary")
    print("--------------------")
    print(f"Failed login attempts: {failed_logins}")
    print(f"Successful logins: {successful_logins}")


if __name__ == "__main__":
    file_path = "sample.log"
    analyze_log(file_path)
