resource "aws_security_group" "web" {

  ingress {

    from_port = 80
    to_port = 80

    protocol = "tcp"

    cidr_blocks = [
      "0.0.0.0/0"
    ]
  }
}

resource "aws_instance" "web" {

  ami = "ami-123"

  instance_type = "t2.micro"
}