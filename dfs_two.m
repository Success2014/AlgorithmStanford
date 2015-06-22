% DFS
function [] = dfs_two(graph,startpoint)
global explored following leader

explored(startpoint) = 1;
following(startpoint) = leader;

arcEnd = graph((graph(:,1)==startpoint),2); % arc goes from startpoint

for j = 1:length(arcEnd)
    if ~explored(arcEnd(j))
        dfs_two(graph,arcEnd(j));
    end
end

% ftcnt = ftcnt + 1;
% fntym(startpoint) = ftcnt;