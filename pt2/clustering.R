library('stringdist')

## find function of union-find data structure
find <- function(n,clusters){
  name <- NULL
  for (i in 1:length(clusters)){
    if(n %in% clusters[[i]]){
      name <- names(clusters[i])
      break
    }
  }
  name
}



## Kruskal's union-find based algorithm to compute max spacing k-clustering
## Complexity O (|V| log |E|) - same as heap-based prim's algorithm
max_spacing <- function(num_clusters, filename){
  
  input <- read.csv(filename, header = FALSE, sep = " ")
  num_nodes<-input[1, 'V1']
  
  ##Generate graph
  n_data <- input[2:nrow(input),]
  k <- nrow(n_data)-1
  
  #sort by increasing order, i. e. nearest vertices
  sorted_data <- n_data[order(n_data$V3),]
  
  #init clusters
  clusters <- list()
  clusters[1:num_nodes] <- 1:num_nodes
  names(clusters) <- 1:num_nodes
  
  i <- 1
  n <- length(clusters)
  
  #while number of desired clusters not reached, then group nearest vertices
  while(n != num_clusters){
  
    edge <- sorted_data[i,]
    
    #find operation
    c1 <- find(edge$V1,clusters)
    c2 <- find(edge$V2,clusters)
  
    i <- i + 1
    
    #if nodes are already in same cluster, skip edge
    if(c1 == c2){
      next
    }
    
    #union operation
    clusters[[c1]] <- c(clusters[[c1]], clusters[[c2]])
    clusters[c2] <- list(NULL)
    
    #update number of non-empty clusters
    n <- length(Filter(Negate(is.null),clusters))
  }
  
  #delete empty clusters
  filtered <- Filter(Negate(is.null),clusters)
  
  #retrieve value that minimizes max spacing
  min <- c()
  for (i in 1:length(filtered)){
    result <- subset(n_data, V1 %in% filtered[[i]] & V2 %in% unlist(filtered[-i]), select = V3)
    min <- c(min,as.vector(result$V3))
  }
  min[order(min)][1]
}