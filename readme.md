A `.bib` sorting tool defaults to sorting by the first letter of the article title, aiming to prevent the same reference from being cited twice.

`.bib` 排序工具, 默认是按照文章标题的第一个字母排序, 目标是为了避免同一篇文献被引用两次. 

> 排序规则: 
> 1. 先按年份升序，年份相同时按 title 首字母升序. (--sort y)
> 2. 按照论文名称的首字母排序, 用于排查同一篇文献被引用两次 (--sort t)

运行:

```
python main.py --input refs.bib --output sorted_refs.bib
```

