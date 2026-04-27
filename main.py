from spam_detection.services.detector_factory import DetectorFactory
from spam_detection.services.result_storage import ResultStorage
from spam_detection.services.spam_system import SpamDetectionSystem
from spam_detection.utils.file_manager import FileManager


def build_system() -> SpamDetectionSystem:
    detector_names = ["keyword", "blacklist", "frequency"]
    detectors = [DetectorFactory.create_detector(name) for name in detector_names]
    return SpamDetectionSystem(detectors)


def main() -> None:
    print("Spam Messages Detecting System")
    input_path = input("Enter CSV file path (default: data/messages.csv): ").strip()
    output_path = input(
        "Enter result file path (default: results/detection_results.csv): "
    ).strip()

    input_path = input_path or "data/messages.csv"
    output_path = output_path or "results/detection_results.csv"

    file_manager = FileManager()
    storage = ResultStorage()
    system = build_system()

    try:
        messages = file_manager.load_messages(input_path)
    except (FileNotFoundError, ValueError) as error:
        print(f"Error: {error}")
        return

    if not messages:
        print("No messages found in the file.")
        return

    results = [system.analyze_message(message) for message in messages]
    storage.save_results(output_path, results)

    print("\nAnalysis results:")
    for index, result in enumerate(results, start=1):
        print(
            f"{index}. Sender: {result['sender']} | Label: {result['label']} | "
            f"Detected by: {result['detected_by']}"
        )

    print(f"\nResults saved to: {output_path}")


if __name__ == "__main__":
    main()
