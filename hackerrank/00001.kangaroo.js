// function kangaroo(x1, v1, x2, v2) {
//   if (x1 < x2 && v1 <= v2) return "NO";
//   if ((x1 - x2) % (v2 - v1) === 0) return "YES";
//   return "NO";
// }

function kangaroo(x1, v1, x2, v2) {
  if (x1 < x2 && v1 <= v2) return "NO";
  if (x1 == x2) return "YES";

  const dict = Math.abs(x1 - x2);
  while (true) {
    x1 += v1;
    x2 += v2;
    if (Math.abs(x1 - x2) >= dict) break;
  }

  return Math.abs(x1 - x2) == dict ? "YES" : "NO";
}

const tests = [
  // [[0, 3, 4, 2], "YES"],
  // [[0, 3, 0, 2], "YES"],
  // [[0, 2, 5, 3], "NO"],
  [[0, 4, 4, 1], "NO"],
];

for (const [input, output] of tests) {
  r = kangaroo(...input);
  message = r === output ? `\x1b[32mOK` : `\x1b[31mFAILED: ${input}`;
  console.log(message);
}
