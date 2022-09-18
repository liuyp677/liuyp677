
/* 
document.write('写在页面中 <br>')
alert('弹出框')
console.log('日志')
prompt('弹出框输入') 
*/

// 输入并在页面输出
let usr_name = 'a'
document.write(usr_name + '<br>')

document.write('woshji' + usr_name + '<br>')

document.write(`string text line 1
string text line 2` + '<br>')  //无效，看来只能在log里面

console.log(`string text line 1
string text line 2` + '<br>')    //有效，必须反引号

document.write(`shiwos  ${usr_name}` + '<br>')  //有效，必须反引号

console.log(`shiwos  ${usr_name}` + '<br>')  //有效，必须反引号


//数据类型
console.log(Number('10.01'))
console.log(parseInt('10.01')) //注意不能带字母等别的东西，NAN也是数字型
console.log(parseFloat('100px')) //经常用于过滤，但必须是数字打头

console.log(0.1 + 0.2) //最好不要比较小数，会涉及到精度的问题

//数组的增加、删除
let arr = []
console.log(arr.push('q', 'w'))
console.log(arr[0])
arr.unshift('a', 's')
arr.pop()//删除最后一个元素
arr.shift()//删除第一个元素
arr.splice(1, 1)//删除第一个元素之后的一个元素
arr.splice(1) //删除第一个元素之后的所有元素