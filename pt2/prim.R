##Minimum spanning trees
##Spanning tree: no cycles, all connected nodes are spanned
##Computes minimum cost satisfy above criteria

input <- read.csv('edges.txt', header = FALSE, sep = " ")
num_nodes<-input[1, 'V1']
num_edges<-input[1, 'V2']

data <- input[2:nrow(input),]

random_row<-as.numeric(data[sample(1:nrow(data),1),])
all_rows <- as.numeric(data[,1])
X <- c(random_row[1])
V <- c(unique(all_rows))

dict<-split(data,data$V1)

while(all(X,V)==FALSE){
  
  
  
}
