digraph graphname{
    a[label="teacher"] [shape="box"][style="filled", color="black", fillcolor="purple"][penwidth=2.0]   ;
    b[label="student a"] [shape="record"][style="filled", color="black", fillcolor="blue"][penwidth=2.0]   ;
    c[label="student b"] [shape="record"][style="filled", color="black", fillcolor="blue"][penwidth=2.0]   ;
    d[label="student c"][shape="record"][style="filled", color="black", fillcolor="blue"][penwidth=2.0]   ;
    e[label="student d"][shape="record"][style="filled", color="black", fillcolor="blue"][penwidth=2.0]   ;
    f[label="headmaster"] [style="filled", color="black", fillcolor="red"][shape="egg"][penwidth=2.0]   ;
    g[label="director"] [style="filled", color="black", fillcolor="gold"][penwidth=2.0]   
    f -> a,g [style="dashed"][label="manage"];
    a -> b,c,d,e[style="dashed"][label="manage"];
}
