pub fn raindrops(num: i32) -> String {
    let mut result = String::new();

    if num % 3 == 0 {result.push_str("Pling")};
    if num % 5 == 0 {result += "Plang"};
    if num % 7 == 0 {result.push_str("Plong")};

    if result.is_empty() { num.to_string() } else { result }
}
