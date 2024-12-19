package main  
  
import (  
    "fmt"  
    "html/template"  
    "net/http"  
)  
  
func main() {  
    http.HandleFunc("/", homeHandler)  
    http.HandleFunc("/login", loginHandler)  
    http.HandleFunc("/signup", signupHandler)  
    fmt.Println("Server started at http://localhost:8080")  
    http.ListenAndServe(":8080", nil)  
}  
  
func homeHandler(w http.ResponseWriter, r *http.Request) {  
    tmpl := template.Must(template.ParseFiles("templates/home.html"))  
    tmpl.Execute(w, nil)  
}  
  
func loginHandler(w http.ResponseWriter, r *http.Request) {  
    if r.Method == "GET" {  
        tmpl := template.Must(template.ParseFiles("templates/login.html"))  
        tmpl.Execute(w, nil)  
    } else {  
        // 这里处理用户登录逻辑  
        // 真实环境中应该检查用户名和密码，这里简化处理  
        http.Redirect(w, r, "/welcome", http.StatusSeeOther)  
    }  
}  
  
func signupHandler(w http.ResponseWriter, r *http.Request) {  
    if r.Method == "GET" {  
        tmpl := template.Must(template.ParseFiles("templates/signup.html"))  
        tmpl.Execute(w, nil)  
    } else {  
        // 这里处理用户注册逻辑  
        // 真实环境中应该保存用户数据  
        http.Redirect(w, r, "/welcome", http.StatusSeeOther)  
    }  
}  