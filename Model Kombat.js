#### Approach
- Take absolute value of the input seconds, floor to handle fractional inputs.
- Compute hours, minutes, and seconds via division and modulo.
- Zero-pad each component to at least two digits; prefix a minus sign if the original value was negative.

#### TypeScript
```ts
/**
 * Converts a duration in seconds to an HH:MM:SS formatted string.
 * - Handles negative inputs by prefixing '-'.
 * - Floors fractional seconds, does not wrap days (hours can exceed 24).
 */
export function formatDuration(totalSeconds: number): string {
  if (!Number.isFinite(totalSeconds)) {
    throw new Error("Invalid input: seconds must be a finite number.");
  }

  const isNegative = totalSeconds < 0;
  const s = Math.floor(Math.abs(totalSeconds));

  const hours = Math.floor(s / 3600);
  const minutes = Math.floor((s % 3600) / 60);
  const seconds = s % 60;

  const hh = String(hours).padStart(2, "0");
  const mm = String(minutes).padStart(2, "0");
  const ss = String(seconds).padStart(2, "0");

  const result = `${hh}:${mm}:${ss}`;
  return isNegative ? `-${result}` : result;
}
```
