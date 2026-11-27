// EP23 — ஹிட்லர்: வீடில்லாதவனில் இருந்து ராட்சசன் வரை (Hitler: From Homeless to Monster). About 105 minutes, 12 chapters.
// Narration script, source of truth. One file per chapter (script/chNN.mjs); this file joins them in film order.
// One entry per spoken line: [say, tag?, cap?, fx?]
//   say = what the voice reads (numbers spelled out, foreign names in Tamil letters)
//   tag = evidence label on screen: F பதிவான உண்மை · W சாட்சி சொன்னது · S அவரே எழுதியது · H வரலாற்றாசிரியர் கருத்து · O கருத்து
//   cap = caption text when it differs from `say` (digits)
//   fx  = added picture language for this line (film/fx.mjs): stat, big, flash (+strike); cuts: [sentence numbers]; reuse: [shot names]
// Clip ids are N01 … N98 in film order. Hook N01–N02; chapter k owns the eight ids from N(8k−5): ch1 N03–N10, ch2 N11–N18, ch3 N19–N26,
// ch4 N27–N34, ch5 N35–N42, ch6 N43–N50, ch7 N51–N58, ch8 N59–N66, ch9 N67–N74, ch10 N75–N82, ch11 N83–N90, ch12 N91–N98.
// A chapter uses about six of its eight ids; the free ones stay empty. A clip with a `title` opens a chapter (chapter card).
// "S" marks what he himself wrote in Mein Kampf (1925): it is his version, often not confirmed. "W" is what a named witness said later.
import ch00 from "./ch00.mjs";
import ch01 from "./ch01.mjs";
import ch02 from "./ch02.mjs";
import ch03 from "./ch03.mjs";
import ch04 from "./ch04.mjs";
import ch05 from "./ch05.mjs";
import ch06 from "./ch06.mjs";
import ch07 from "./ch07.mjs";
import ch08 from "./ch08.mjs";
export const TAGS = { F: "பதிவான உண்மை", W: "சாட்சி சொன்னது", S: "அவரே எழுதியது", H: "வரலாற்றாசிரியர் கருத்து", O: "கருத்து" };
export const TITLE = ["ஹிட்லர்", "வீடில்லாதவனில் இருந்து ராட்சசன் வரை"];
export const CHAPTERS = [
  ["0", "HOOK", "வியன்னா, 1909"], ["1", "1889–1907", "அம்மா செல்லம்"], ["2", "1908–1913", "வீடில்லாதவன்"], ["3", "1914–1918", "போர் கொடுத்த வீடு"],
  ["4", "1919–1923", "குரல்"], ["5", "1924–1929", "சிறையும் காத்திருப்பும்"], ["6", "1929–1933", "நெருக்கடி"], ["7", "1933–1934", "பதினெட்டு மாசம்"],
  ["8", "1934–1938", "ஒரு நாடு பின்னாடி போச்சு"], ["9", "1939–1941", "போர்"], ["10", "1941–1945", "பேரழிவு"], ["11", "1942–1944", "சரிவு"], ["12", "1945", "பதுங்கு குழி"],
];
export const CLIPS = [...ch00, ...ch01, ...ch02, ...ch03, ...ch04, ...ch05, ...ch06, ...ch07, ...ch08];
