package main  
  
import (  
    "database/sql"  
    "fmt"  
    "net/http"  
    "regexp"  
  
    _ "github.com/denisenkom/go-mssqldb"  
)  
  
func main() {  
    http.HandleFunc("/register", registerHandler)  
    http.ListenAndServe(":5500", nil)  
}  
  
func registerHandler(w http.ResponseWriter, r *http.Request) {  
    if r.Method != "POST" {  
        http.Error(w, "Invalid request method", http.StatusMethodNotAllowed)  
        return  
    }  
  
    // 解析表单数据  
    r.ParseForm()  
    username := r.FormValue("username")  
    password := r.FormValue("password")  
  
    // 验证用户名和密码  
    if !isValid(username) || !isValid(password) {  
        http.Error(w, "Username or Password does not meet requirements", http.StatusBadRequest)  
        return  
    }  
  
    // 连接数据库并插入数据  
    if err := insertUser(username, password); err != nil {  
        http.Error(w, "Failed to register user", http.StatusInternalServerError)  
        return  
    }  
  
    fmt.Fprintln(w, "User registered successfully")  
}  
  
func isValid(s string) bool {  
    if len(s) < 8 {  
        return false  
    }  
    match, _ := regexp.MatchString("^[a-zA-Z0-9]+$", s)  
    return match  
}  
  
func insertUser(username, password string) error {  
    // 使用您的Azure数据库连接信息  
    connString := "server=<yourserver>;user id=<yourusername>;password=<yourpassword>;database=<yourdbname>"  
    db, err := sql.Open("mssql", connString)  
    if err != nil {  
        return err  
    }  
    defer db.Close()  
  
    // 插入用户  
    _, err = db.Exec("INSERT INTO Users (Username, Password) VALUES (?, ?)", username, password)  
    return err  
}  