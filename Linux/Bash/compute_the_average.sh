read iteration

sum=0
for ((i=0; i < $iteration; i++)); do
    read input
    sum=$((sum+input))
done

printf "%.3f" `echo $sum/$iteration | bc -l`
