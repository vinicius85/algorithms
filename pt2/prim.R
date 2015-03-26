##Minimum spanning trees
##Spanning tree: no cycles, all connected nodes are spanned
##Computes minimum cost satisfy above criteria

prim <- function(){
  
  input <- read.csv('edges-text.txt', header = FALSE, sep = " ")
  num_nodes<-input[1, 'V1']
  num_edges<-input[1, 'V2']
  
  data <- input[2:nrow(input),]
  
  random_row<-as.numeric(data[sample(1:nrow(data),1),])
  all_rows <- as.numeric(data[,1])
  X <- c(random_row[1])
  V <- c(unique(all_rows))
  A <- c()
  
  cost <- 0
  
  i <- 0
  
  while(length(intersect(X,V))!=length(V)){
    
    k <- X[1]
    e <- subset(data, V1==k)
    
    if(!e[2] %in% A){
      A <- c(e[2],A)
      X <- c(e[1],X)
      
      cost <- cost + e[3]
    }
    
    i<- i+1
    
  }
  
  print(paste("MST Cost" ,cost, sep = " "))
}