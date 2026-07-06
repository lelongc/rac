# AutoEVE Prompting Guidelines

When generating a "Thần chú" (Prompt) for the AutoEVE Web Tool, you MUST strictly adhere to the following formatting rules. Failure to do so will break the backend LLM parser.

1. **Strict Hierarchical Formatting**: Always use explicit bullet points (`-` for parent items, `+` for child items). Do NOT output flat text or remove these symbols.
2. **Explicit IP Assignments**: When assigning IPs, use the format: `+ R1 (s1/0): 192.168.23.1` or `+ Dải X: R1 (e0/1) IP, VPC7 IP`.
3. **Explicit Routing Syntax**: Do not use vague conversational language for OSPF or Routing. Use exact syntax or strict structured phrasing.
   - Good: `+ Trên R1: Quảng bá mạng 192.168.23.0 (thuộc area 0) và mạng 10.0.1.0 (thuộc area 1).`
   - Good: `+ Trên R1: Cấu hình lệnh network 192.168.23.0 0.0.0.255 area 0`
   - Bad: `+ R1: Quảng bá mạng 192.168.23.0 vào Area 0...`
4. Always remind the user NEVER to delete the bullet points (`-`, `+`) when they copy-paste the text.
