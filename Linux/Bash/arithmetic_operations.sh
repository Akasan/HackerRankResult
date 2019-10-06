# I refered this answer from discussion, because I couldn't make result myself

read exp
printf "%.3f\n" `echo $exp | bc -l`
