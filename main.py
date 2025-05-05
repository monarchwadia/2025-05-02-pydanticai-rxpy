import reactivex as rx
from reactivex import operators as ops

def main():
    source = rx.of("Hello from 2025-05-02-pydanticai-rxpy!")
    composed = source.pipe(
        ops.do_action(
            on_next=lambda x: print(f"Original: {x}"),
            on_error=lambda e: print(f"Error: {e}"),
            on_completed=lambda: print("Completed!"),
        ),
        ops.map(lambda x: x.upper()),
        ops.do_action(
            on_next=lambda x: print(f"Uppercase: {x}"),
            on_error=lambda e: print(f"Error: {e}"),
            on_completed=lambda: print("Completed!"),
        )
    )
    composed.subscribe(
        on_next=lambda x: print(f"Final Output: {x}"),
        on_error=lambda e: print(f"Error: {e}"),
        on_completed=lambda: print("Completed!"),
    )


if __name__ == "__main__":
    main()
