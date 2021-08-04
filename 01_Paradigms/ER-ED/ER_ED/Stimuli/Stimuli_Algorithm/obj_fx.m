function [ fit ] = obj_fx( cat_mat, data )
%OBJ_FX calculates the fit
%   cat_mat - vector with the cluster id for every item

m_cluster = zeros(max(cat_mat), size(data,2));

for i=1:max(cat_mat)
    m_cluster(i, :) = mean(data(cat_mat==i, :));   
end

m_cluster_std = std(m_cluster);



fit = sum(m_cluster_std(2:3));

end

