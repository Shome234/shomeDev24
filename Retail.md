### controler for admin using repository and service layer
```
 public class AdminController : Controller
 {
     private readonly IUserService _userService;

     public AdminController(IUserService userService)
     {
         _userService = userService;
     }
     public async Task<IActionResult> Index()
     {
         return View(await _userService.GetAllUsersAsync());
     }

     [HttpGet]
     public async Task<IActionResult> Create()
     {
         return View();
     }

     [HttpPost]
     public async Task<IActionResult> Create(User user)
     {
         if (!ModelState.IsValid)
         {
             return BadRequest(ModelState);
         }
         await _userService.AddUserAsync(user);
         return RedirectToAction("Index");
     }

     [HttpPut("{userId}")]
     public async Task<IActionResult> Edit(int userId,User user)
     {
         if (userId == user.UserId || !ModelState.IsValid)
         {
             return BadRequest(ModelState);
         }
         var existingUser=await _userService.GetUserByIdAsync(userId);
         if (existingUser == null)
         {
             return NotFound();
         }
         await _userService.UpdateUserAsync(user);
         return RedirectToAction("Index");
     }

     [HttpDelete("{userId}")]
     public async Task<IActionResult> Delete(int userId)
     {
         var existingUser=await _userService.GetUserByIdAsync(userId);   
         if(existingUser == null)
         {
             return NotFound();
         }
         await _userService.DeleteUserAsync(userId);
         return RedirectToAction("Index");
     }
 }
```
