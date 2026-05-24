from report_writer import save_report
from analyzer import process_open_issues, process_closed_issues
from exceptions import GithubClientError, ClaudeClientError

def main():
    print("starting report generation...")
    
    try:
        print("fetching closed issues...")
        closed_path = save_report(process_closed_issues(), "closed_issues_report")
        print(f"saved to: {closed_path}")

        print("fetching open issues...")
        open_path = save_report(process_open_issues(), "open_issues_report")
        print(f"saved to: {open_path}")

        print("success")

    except (GithubClientError, ClaudeClientError) as e:
        print(f"api error: {str(e)}")
        
    except (ValueError, RuntimeError) as e:
        print(f"file error: {str(e)}")
        
    except Exception as e:
        print(f"unexpected error: {str(e)}")


if __name__ == "__main__":
    main()