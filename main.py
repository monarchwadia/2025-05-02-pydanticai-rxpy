import reactivex as rx
from reactivex import operators as ops

def main():
    source = rx.of(
        # don't tell me how to live my life
        "don't",
        "tell",
        "me",
        "how",
        "to",
        "live",
        "my",
        "life"
    )
    composed = source.pipe(
        ops.do_action(
            on_next=lambda x: print(f"Original: {x}"),
            on_error=lambda e: print(f"Error: {e}"),
            on_completed=lambda: print("Completed: #1"),
        ),
        ops.map(lambda x: x.upper()),
        ops.do_action(
            on_next=lambda x: print(f"Uppercase: {x}"),
            on_error=lambda e: print(f"Error: {e}"),
            on_completed=lambda: print("Completed: #2"),
        )
    )
    composed.subscribe(
        on_next=lambda x: print(f"Final Output: {x}"),
        on_error=lambda e: print(f"Error: {e}"),
        on_completed=lambda: print("Completed: #3"),
    )


if __name__ == "__main__":
    main()
