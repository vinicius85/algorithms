## Prim's Algorithm - Minimum spanning trees
## Spanning tree: 1. no cycles, 2. all connected nodes are spanned
## Compute minimum cost which satisfies above criteria

## Time complexity: O(|E|log|V|), if adjacency list is a heap ( which is not the case :) )

## Dijkstra shortest path only computes minimal cost between s->t. Special case of Prim's

prim <- function(){
  
  #Read file
  input <- read.csv('edges.txt', header = FALSE, sep = " ")
  num_nodes<-input[1, 'V1']
  num_edges<-input[1, 'V2']
  
  #Generate undirected graph
  n_data   <- input[2:nrow(input),]
  i_data <- data.frame(n_data$V2, n_data$V1, n_data$V3)
  colnames(i_data) <- c('V1','V2','V3')
  data <- rbind(n_data,i_data)
  
  #Init step
  random_row<-as.numeric(data[sample(1:nrow(data),1),])
  all_rows <- as.numeric(data[,1])
  X <- c(random_row[1])
  V <- c(unique(all_rows))
  E <- c() 
  cost <- 0
  
  #main loop
  while(length(intersect(X,V))!=length(V)){
    
    edges <- subset(data, !row.names(data) %in% E & V1 %in% X & !V2 %in% X)
    min_e <- edges[order(edges$V3),][1,]
  
    X <- c(X,as.numeric(min_e[2]))
    E <- c(E,as.numeric(row.names(min_e)))
    cost <- cost + as.numeric(min_e[3])
    
  }
  
  print(paste("MST Cost" ,cost, sep = " "))
}