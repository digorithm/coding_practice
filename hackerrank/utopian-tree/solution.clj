; Problem Statement

; The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.

; Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of spring. How tall will her tree be after N growth cycles?

; Input Format

; The first line contains an integer, T, the number of test cases. 
; T subsequent lines each contain an integer, N, denoting the number of cycles for that test case.

; Constraints 
; 1≤T≤10 
; 0≤N≤60
; Output Format

; For each test case, print the height of the Utopian Tree after N cycles. Each height must be printed on a new line.


; First solution

(defn walk-cycles [n]
  (if (= 0 n)
      (println 1)
      (let [meters (atom 1)]
        (doseq [i (range 1 (inc n))]
          (if (even? i)
              (swap! meters inc)
              (swap! meters #(* % 2))))
        (println @meters))))