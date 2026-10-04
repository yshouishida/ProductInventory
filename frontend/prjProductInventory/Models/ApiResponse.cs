using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace prjProductInventory.Models
{
    public class ApiResponse<T>
    {
        public string message { get; set; }
        public T data { get; set; }
    }
}
