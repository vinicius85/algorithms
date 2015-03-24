#Compute sum of completion times
completionTimes <- function(jobs, greedy){
  #Sort jobs by decreasing diff order
  sorted_jobs <- jobs[order(-greedy, -jobs$weight),]
  
  completionTimes <- 0;
  sumCompletionTimes <- 0;
  
  for(i in 1:nrow(sorted_jobs)){
    w <- sorted_jobs[i,'weight']
    l <- sorted_jobs[i,'length']
    completionTimes <- completionTimes + l
    sumCompletionTimes <- sumCompletionTimes + (w*completionTimes)
  } 
  sumCompletionTimes
}

#Read jobs from input file
jobs <- read.csv('jobs2.txt', header = TRUE, sep = " ")

#Compute (w-l) and (w/l)
jobs$diff <- jobs$weight - jobs$length
jobs$div  <- jobs$weight / jobs$length

sumCompletionTimes <- completionTimes(jobs,jobs$diff)
print(paste("Completion diff ",sumCompletionTimes, sep = " "))

sumCompletionTimes <- completionTimes(jobs,jobs$div)
print(paste("Completion div ",sumCompletionTimes, sep = " "))