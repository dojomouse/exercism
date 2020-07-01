pub fn reply(query:&str) -> &str {
    match query {
        x if x.is_empty() => "Fine. Be that way!",
        x if x.ends_with("?") => "Sure.",
        x if x == x.to_uppercase() => "Whoa, chill out!",
        _ => "Whatever.",
    }
}
