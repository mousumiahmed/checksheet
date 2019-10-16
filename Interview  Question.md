​							Interview  Question



Q.Difference bet transition and transform

For example, the below styles will rotate a div over a period of 1 second upon hover.



```css
div {
  width: 100px;
  height: 100px;
  background-color: yellow;
  transition: transform 1s;
  /* timing function and delay not specified */
}
div:hover {
  transform: rotate(30deg);
}
```