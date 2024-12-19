package main  
  
import (  
    "fmt"  
    "net/http"  
)  
  
func main() {  
    // 设置处理函数  
    http.HandleFunc("/login", loginHandler)  
  
    // 启动服务器  
    fmt.Println("Server is running at http://localhost:8080")  
    http.ListenAndServe(":5500", nil)  
}  
  
// 处理登录的函数  
func loginHandler(w http.ResponseWriter, r *http.Request) {  
    // 确保我们只在POST请求中处理数据  
    if r.Method == "POST" {  
        // 解析表单数据  
        err := r.ParseForm()  
        if err != nil {  
            http.Error(w, "Error parsing the form", http.StatusInternalServerError)  
            return  
        }  
  
        // 获取用户名和密码字段  
        username := r.FormValue("username")  
        password := r.FormValue("password")  
  
        // 在这里添加你的验证逻辑  
        if username == "admin" && password == "password123" {  
            fmt.Fprintf(w, "Login successful")  
        } else {  
            fmt.Fprintf(w, "Invalid username or password")  
        }  
    } else {  
        // 如果不是POST请求，返回一个错误  
        http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)  
    }  
}  