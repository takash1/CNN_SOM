library(kohonen)
data <- read.csv("features.csv", header=F)
set.seed(10)
music_som <- som(scale(data[,2:101]), grid=somgrid(5, 5, "hexagonal"), rlen=3000)

# Training progress
# plot(music_som, type="changes", main="chage of similarity")

# Visualize
png("som.png")
plot(music_som, type="mapping", labels=data[,1], main="X Japan SOM")
dev.off()
