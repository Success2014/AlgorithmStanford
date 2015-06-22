clear,clc

graph = importdata('SCC.txt');
n = length(unique(graph));

[~, fntym] = dfs_loop([graph(:,2) graph(:,1)],n);
following = dfs_loop_two(graph,n,fntym);

leaders = unique(following);
numFollowers = zeros(length(leaders),1);
for l = 1:length(leaders)
    numFollowers(l) = sum(following==leaders(l));
end

result = sort(numFollowers,'descend');