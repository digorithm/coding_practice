; Problem Statement
;
; Pawel and Shaka recently became friends. On their planet, it is believed that their friendship will last forever, if they merge their favorite strings and etch it on the surface of a stone.

; So we will mingle their favorite strings. The lengths of their favorite strings is same (say n). Mingling two strings, P=p1p2…pn and Q=q1q2…qn, both of length n, will result in creation of a new string R of length 2×n. It will have the following structure:

; R=p1q1p2q2…pnqn
; You are given two strings P (favorite of Pawel) and Q (favorite of Shaka), find the mingled string R.

; Input 
; First line of input contains string P, and second line contains Q. 

; Output 
; Print string R.


; first attempt, it worked.
(defn vect-of-chars [s] (vec s))

(defn ming [p q]
  (let [s (map vect-of-chars [p q])]
    (apply str 
      (for [i (range (count p))]
        (str (get p i) (get q i))))))


; second attempt, worked faster, incredibly simpler
(defn ming2 [p q]
  (apply str (map str p q)))


(println (ming2 (read-line) (read-line)))
