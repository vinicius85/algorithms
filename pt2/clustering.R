union <- function(c1,c2){
  c12 <- c(c1,c2)
  c12
}

find <- function(x,clusters){
  cluster <- NULL
  for(c in clusters){
    if(x %in% c){
      cluster <- c
    }
  }
  cluster
}

## Kruskal's union-find algorithm to compute max spacing k-clustering
## Complexity O (|V| log |E|) same as heap-based prim's algorithm
max_spacing <- function(num_clusters){
  
  input <- read.csv('cluster-test.txt', header = FALSE, sep = " ")
  num_nodes<-input[1, 'V1']
  
  ##Generate undirected graph
  n_data <- input[2:nrow(input),]
  k <- nrow(n_data)-1
  
  #i_data <- data.frame(n_data$V2, n_data$V1, n_data$V3)
  #colnames(i_data) <- c('V1','V2','V3')
  #data <- rbind(n_data,i_data)
  
  #sort by increasing order
  sorted_data <- n_data[order(n_data$V3),]
  
  #init clusters
  clusters <- list()
  clusters[1:k] <- 1:k
  
  i <- 0
  n <- 0
  
  while(n != num_clusters){
  
    edge <- sorted_data[i+1,]
    clusters[[edge$V1]] <- c(clusters[[edge$V1]], clusters[[edge$V2]])
    clusters[edge$V2] <- list(NULL)

    n <- length(Filter(Negate(is.null),clusters))
    i <- i + 1
  }
  
  filtered <- Filter(Negate(is.null),clusters)
  
  for(list in filtered){
    for(element in list){
      print(element)
    }
  }
}