#Read jobs from input file
jobs <- read.csv('jobs.txt', header = TRUE, sep = " ")

#Compute (w-l) and (w/l)
jobs$diff <- jobs$weight - jobs$length
jobs$div <- jobs$weight/jobs$length

#Sort jobs by decreasing order
sorted_jobs <- jobs[order(-jobs$diff, -jobs$weight),]

sumCompleted <- 0;

for(job in sorted_jobs){
  sumCompleted <- sumCompleted + (job$weight*job$diff)
}

print('completed (diff)'+sumCompleted)